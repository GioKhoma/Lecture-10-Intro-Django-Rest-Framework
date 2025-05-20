🚀 Django Lecture 10 Summary  
Topics Covered:

🔗 What is API & RESTful API  
⚙️ Django REST Framework (DRF) Overview  
🧩 Serializers  
📄 Views: APIView, GenericAPIView, ViewSets  
🛠️ Building a To-Do App with CRUD  
📝 Practical Examples  

---

🔗 1. What is API & RESTful API  
API (Application Programming Interface) — a way for software to communicate.  
RESTful API — architectural style using HTTP methods (GET, POST, PUT, DELETE) with stateless, resource-based URLs.  

---

⚙️ 2. Django REST Framework (DRF)  
DRF is a powerful toolkit for building Web APIs on top of Django.  

🧠 Why DRF?  
- Simplifies API development  
- Provides serializers for converting data  
- Supports permissions, throttling  
- Includes browsable API interface for testing  

---

🧩 3. Serializers  
Serializers convert complex data like Django QuerySets into JSON and vice versa.  
- Similar to Django Forms  
- Validate input data  
- Used in Views to parse requests and format responses  

---

📄 4. Views in DRF  
- **APIView:** Basic class-based views with manual method definitions  
- **GenericAPIView:** Adds queryset and serializer handling, base for generic views  
- **ViewSets:** Group related views (list, create, update, delete) in one class, works with routers for URL routing  

---

🛠️ 5. Building a To-Do App (CRUD)  
- Create Task model with fields like title and description  
- Write serializer for validation and data conversion  
- Use ViewSets and routers for clean URLs  
- Implement permissions so only owners can modify tasks  

---

📝 6. Practical Examples  
- Using APIView for custom logic  
- Using GenericAPIView for reusable patterns  
- Using ModelViewSet + routers for quick CRUD APIs  
- Adding custom permissions and auto-assigning owners on create  

---

🎯 Goal  
By the end of this lecture, you will be able to:  
- Understand REST principles and API design  
- Use Django REST Framework’s main components effectively  
- Build secure and scalable APIs with permissions  
- Implement real-world API features like CRUD operations using ViewSets  

---
