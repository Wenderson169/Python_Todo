while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            #new_todos = [item.strip('\n') for item in todos]

            for index, todo in enumerate(todos):
                todo = todo.strip('\n')
                print(f"{index + 1}- {todo}")

        case 'edit':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(number - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list"
            print(message)

        case 'exit':
            break

        case _:
            print("This option doesn't exist!")

print("Bye!")
