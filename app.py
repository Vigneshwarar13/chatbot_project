from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined questions and answers for college information
college_info = {
    "How to contact SRM Ramapuram?": "You can contact SRM Ramapuram at their official contact page: https://srmrmp.edu.in/contact",
    "What is the fee structure at SRM Ramapuram?": "The fee structure varies by course. Details can be found here: https://srmrmp.edu.in/admission/fee-structure",
    "What courses are offered at SRM Ramapuram?": "Programs offered can be viewed here: https://srmrmp.edu.in/academics/courses-offered",
    "Where can I find the syllabus?": "Find syllabi for various programs here: https://srmrmp.edu.in/academics/syllabus",
    "Where is the exam timetable?": "Exam schedules are posted here: https://srmrmp.edu.in/academics/exam-timetable",
    "What are the hostel facilities like?": "Hostel facilities info can be found here: https://srmrmp.edu.in/campus-life/hostel-facilities",
    "What about placements at SRM Ramapuram?": "Placement information is available at: https://srmrmp.edu.in/placements",
    "What is the ranking of SRM Ramapuram?": "SRMIST's national rankings are listed here: https://srmrmp.edu.in/about-us/rankings",
    "What management does SRM Ramapuram have?": "Details on management can be found here: https://srmrmp.edu.in/administration",
    "What are the transport facilities available?": "Transport facilities and routes can be checked here: https://srmrmp.edu.in/campus-life/transport-facilities",
    "Where is SRM Ramapuram located?": "SRM Ramapuram is located at 3, Veeraraghavapuram, Ramapuram, Chennai, Tamil Nadu 600089, India."
}

# Random tech-related questions and answers
tech_questions = {
   "What is the Internet of Things (IoT)?": "IoT refers to a network of interconnected devices that communicate and exchange data.",
    "What is machine learning?": "Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without explicit programming.",
    "What is a blockchain?": "A blockchain is a distributed ledger technology that ensures secure, transparent, and tamper-proof transactions.",
    "What is the difference between AI and machine learning?": "AI encompasses a broader range of technologies, while machine learning focuses on algorithms that learn from data.",
    "What is cloud computing?": "Cloud computing is the delivery of computing services over the internet, allowing for on-demand access to resources.",
    "What is big data?": "Big data refers to extremely large datasets that can be analyzed computationally to reveal patterns, trends, and associations.",
    "What are microservices?": "Microservices are an architectural style that structures an application as a collection of loosely coupled services.",
    "What is a RESTful API?": "A RESTful API is an application programming interface that uses HTTP requests to access and manipulate data.",
    "What is DevOps?": "DevOps is a set of practices that combines software development and IT operations to shorten the systems development life cycle.",
    "What is an agile methodology?": "Agile is an iterative approach to software development that emphasizes flexibility and customer satisfaction.",
    "What is a database?": "A database is an organized collection of structured information that can be easily accessed, managed, and updated.",
    "What is SQL?": "SQL, or Structured Query Language, is a programming language used to manage and manipulate relational databases.",
    "What is NoSQL?": "NoSQL refers to non-relational database management systems that store data in a format other than tables.",
    "What is cybersecurity?": "Cybersecurity involves protecting systems, networks, and programs from digital attacks.",
    "What is phishing?": "Phishing is a type of cyber attack that involves tricking individuals into revealing sensitive information.",
    "What is a VPN?": "A VPN, or Virtual Private Network, is a service that creates a secure connection over the internet.",
    "What is a DDoS attack?": "A DDoS attack involves overwhelming a server or network with traffic to disrupt services.",
    "What is artificial intelligence (AI)?": "AI is the simulation of human intelligence in machines that are programmed to think and learn.",
    "What is augmented reality (AR)?": "AR is an interactive experience where real-world environments are enhanced by computer-generated content.",
    "What is virtual reality (VR)?": "VR is a simulated experience that can be similar to or completely different from the real world.",
    "What is a compiler?": "A compiler is a program that translates source code written in a programming language into machine code.",
    "What is an operating system?": "An OS is software that manages computer hardware and software resources.",
    "What is software development life cycle (SDLC)?": "SDLC is a process for planning, creating, testing, and deploying software applications.",
    "What is version control?": "Version control is a system that records changes to files over time, allowing you to recall specific versions.",
    "What is Git?": "Git is a distributed version control system used to track changes in source code during software development.",
    "What is a framework?": "A framework is a platform for developing software applications that provides predefined classes and functions.",
    "What is a library?": "A library is a collection of precompiled routines that a program can use.",
    "What is Agile Scrum?": "Scrum is an Agile framework for managing complex software development with iterative and incremental practices.",
    "What is a software bug?": "A bug is an error in software that causes it to produce incorrect or unexpected results.",
    "What is a patch?": "A patch is a piece of software designed to update a computer program or its supporting data.",
    "What is a load balancer?": "A load balancer is a device that distributes network or application traffic across multiple servers.",
    "What is middleware?": "Middleware is software that acts as a bridge between different applications or services.",
    "What is an IDE?": "An IDE, or Integrated Development Environment, is a software application that provides comprehensive facilities for software development.",
    "What is a mobile app?": "A mobile app is a software application designed to run on mobile devices like smartphones and tablets.",
    "What is a web server?": "A web server is a computer that stores and serves web pages to clients over the internet.",
    "What is responsive design?": "Responsive design is an approach to web design that makes web pages render well on a variety of devices.",
    "What is SEO?": "SEO, or Search Engine Optimization, is the practice of optimizing web content to improve its visibility in search engines.",
    "What is a URL?": "A URL, or Uniform Resource Locator, is the address used to access resources on the internet.",
    "What is HTTP?": "HTTP, or Hypertext Transfer Protocol, is the foundation of data communication on the web.",
    "What is HTTPS?": "HTTPS is a secure version of HTTP that uses encryption to protect data during transmission.",
    "What is a cookie?": "A cookie is a small piece of data stored on the user's computer by the web browser while browsing a website.",
    "What is a session?": "A session is a temporary and interactive information interchange between two or more communicating devices.",
    "What is a domain name?": "A domain name is the human-readable address of a website, used to identify an IP address.",
    "What is machine vision?": "Machine vision is a technology that enables computers to interpret and understand visual information from the world.",
    "What is a heuristic algorithm?": "A heuristic algorithm is a problem-solving method that uses a practical approach to find solutions quickly.",
    "What is a neural network?": "A neural network is a series of algorithms that mimic the operations of a human brain to recognize patterns.",
    "What is quantum computing?": "Quantum computing is a type of computation that uses quantum-mechanical phenomena to perform operations on data.",
    "What is edge computing?": "Edge computing processes data near the source of data generation rather than relying on a central data center.",
    "What is data mining?": "Data mining is the practice of examining large datasets to uncover hidden patterns and insights.",
    "What is a chatbot?": "A chatbot is a software application that simulates human conversation through voice commands or text chats.",
    "What is user experience (UX)?": "UX refers to a person's overall experience using a product, especially in terms of how enjoyable or accessible it is.",
    "What is user interface (UI)?": "UI is the space where user interactions with a computer or software application occur.",
    "What is a digital twin?": "A digital twin is a virtual representation of a physical object or system that simulates its real-world counterpart."
}

# Subject-specific questions and answers
subject_info = {
  "design thinking": {
        "What is Design Thinking?": "Design Thinking is a user-centered approach to solving problems by focusing on understanding the user's needs.",
        "What are the phases of Design Thinking?": "The phases include Empathize, Define, Ideate, Prototype, and Test.",
        "What is empathy in Design Thinking?": "Empathy involves understanding the user's feelings and experiences to inform design decisions.",
        "What is prototyping?": "Prototyping is the process of creating an early model of a product to test concepts.",
        "How is Design Thinking different from traditional design?": "Design Thinking emphasizes user feedback and iterative design over linear processes.",
        "What role does feedback play in Design Thinking?": "Feedback is crucial for refining ideas and ensuring they meet user needs.",
        "What is the goal of Ideation?": "The goal of Ideation is to generate a wide range of ideas and solutions.",
        "How can you define a problem statement?": "A problem statement articulates the issue you want to address in a clear and concise way.",
        "What is user persona?": "User personas are fictional characters that represent different user types in a targeted demographic.",
        "What is a user journey map?": "A user journey map visualizes the steps a user takes to complete a task or achieve a goal."
    },
    "operating system": {
        "What is an Operating System?": "An OS is software that manages computer hardware and software resources.",
        "What are the main functions of an OS?": "Functions include process management, memory management, file system management, and device management.",
        "What is process management?": "Process management handles the creation, scheduling, and termination of processes.",
        "What is a thread?": "A thread is the smallest unit of processing that can be scheduled by an OS.",
        "What is a deadlock?": "A deadlock occurs when two or more processes are unable to proceed because each is waiting for the other to release resources.",
        "What is virtual memory?": "Virtual memory allows an OS to use hard disk space to simulate additional RAM.",
        "What is a file system?": "A file system manages how data is stored and retrieved on storage devices.",
        "What is multitasking?": "Multitasking allows multiple processes to run concurrently on a computer.",
        "What is a kernel?": "The kernel is the core part of an OS, responsible for managing system resources and communication between hardware and software.",
        "What is an interrupt?": "An interrupt is a signal to the processor emitted by hardware or software indicating an event that needs immediate attention."
    },
    "data structure": {
        "What is a Data Structure?": "A data structure is a way of organizing and storing data for efficient access and modification.",
        "What is a linked list?": "A linked list is a linear data structure where elements are stored in nodes connected by pointers.",
        "What is a stack?": "A stack is a linear data structure that follows Last In First Out (LIFO) order.",
        "What is a queue?": "A queue is a linear data structure that follows First In First Out (FIFO) order.",
        "What is a binary tree?": "A binary tree is a hierarchical structure where each node has at most two children.",
        "What is a hash table?": "A hash table is a data structure that implements an associative array abstract data type, mapping keys to values.",
        "What is a graph?": "A graph is a collection of nodes (vertices) and edges connecting pairs of nodes.",
        "What is dynamic programming?": "Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems.",
        "What are arrays?": "Arrays are collections of items stored at contiguous memory locations.",
        "What is recursion?": "Recursion is a programming technique where a function calls itself to solve a problem."
    },
    "computer organization": {
        "What is Computer Organization?": "It refers to the operational units and their interconnections that realize the architectural specifications.",
        "What is a CPU?": "The Central Processing Unit (CPU) is the primary component that executes instructions and processes data.",
        "What are registers?": "Registers are small, high-speed storage locations in the CPU used to hold temporary data and instructions.",
        "What is cache memory?": "Cache memory is a smaller, faster type of volatile memory that provides high-speed data access to the CPU.",
        "What is the function of the ALU?": "The Arithmetic Logic Unit (ALU) performs arithmetic and logical operations.",
        "What is the control unit?": "The control unit directs the operation of the processor, managing the flow of data within the CPU.",
        "What is the purpose of an instruction set?": "An instruction set is a collection of instructions that the CPU can execute.",
        "What are buses in computer organization?": "Buses are communication systems that transfer data between components of a computer.",
        "What is memory hierarchy?": "Memory hierarchy is a structure that uses multiple memory types to improve performance and storage efficiency.",
        "What is pipelining?": "Pipelining is a technique where multiple instruction phases are overlapped to improve CPU throughput."
    },
    "advanced programming": {
        "How do you define a function in Python?": "In Python, a function is defined using the `def` keyword followed by the function name and parentheses.",
        "What is polymorphism in Java?": "Polymorphism allows methods to do different things based on the object it is acting upon.",
        "What is a class in Python?": "A class is a blueprint for creating objects that defines attributes and methods.",
        "What is inheritance?": "Inheritance is a mechanism where a new class inherits properties and behavior from an existing class.",
        "What is encapsulation?": "Encapsulation is the bundling of data and methods that operate on that data within one unit, such as a class.",
        "What is a lambda function in Python?": "A lambda function is an anonymous function defined with the `lambda` keyword.",
        "What is exception handling?": "Exception handling is a mechanism to handle runtime errors, ensuring the program continues running.",
        "What is a package in Java?": "A package is a namespace for organizing classes and interfaces in a logical manner.",
        "What is threading?": "Threading allows concurrent execution of two or more threads to maximize CPU utilization.",
        "What is the purpose of `super()` in Python?": "The `super()` function returns a temporary object of the superclass that allows access to its methods."
    }
    # Add more subjects as needed...
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_input = request.form["msg"]
    # Search for an answer in college info, tech questions, or subject info
    answer = college_info.get(user_input) or tech_questions.get(user_input)
    
    # Check in subject_info if not found
    if not answer:
        for subject, questions in subject_info.items():
            if user_input in questions:
                answer = questions[user_input]
                break

    # Default response if no match found
    if not answer:
        answer = "Sorry, I don't know the answer to that. Please try asking something else!"
    
    return answer

if __name__ == "__main__":
    app.run(debug=True)
