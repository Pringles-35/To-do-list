print("📝 Simple To-Do List")
tasks=[]

while True:
    print("What would you like to do?")
    print("1. Add a task")
    print("2. View my list")
    print("3. Exit")

    choice=input("Enter 1,2, or 3:").strip()

    if choice=="1":
      print("great! Let's get started.")
      task=input("Enter your task:").strip().capitalize()
      tasks.append(task)
      print("✅ Task added!")
      print("yukkah".capitalize())

    elif choice=="2":
      print("Sure!")
      if tasks==[]:
          print("⚠️ Your list is empty!")
      else:
        for task in tasks:
            print("- " + task)
            print("   ")

    elif choice=="3":
      print("👋 Goodbye!")
      break

    else:
      print("❌ Please enter 1, 2, or 3.")
    
