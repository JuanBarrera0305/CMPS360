using System;
using System.Collections.Generic;

class Program
{
    static List<Task> tasks = new List<Task>();
    static int nextId = 1;

    static void Main(string[] args)
    {
        bool running = true;

        while (running)
        {
            Console.Clear();
            Console.WriteLine("To-Do List Application");
            Console.WriteLine("1. Add a Task");
            Console.WriteLine("2. View Tasks");
            Console.WriteLine("3. Remove a Task");
            Console.WriteLine("4. Exit");
            Console.Write("Select an option (1-4): ");
            string? input = Console.ReadLine();

            switch (input)
            {
                case "1":
                    AddTask();
                    break;
                case "2":
                    ViewTasks();
                    break;
                case "3":
                    RemoveTask();
                    break;
                case "4":
                    running = false;
                    break;
                default:
                    Console.WriteLine("Invalid option. Please try again.");
                    break;
            }
        }
    }

    static void AddTask()
    {
        Console.Write("Enter task description: ");
        string? description = Console.ReadLine();
        
        if (string.IsNullOrWhiteSpace(description))
        {
            Console.WriteLine("Task description cannot be empty.");
            return;
        }

        Task newTask = new Task(nextId++, description);
        tasks.Add(newTask);
        Console.WriteLine("Task added successfully.");
        Console.ReadKey();
    }

    static void ViewTasks()
    {
        if (tasks.Count == 0)
        {
            Console.WriteLine("No tasks to display.");
        }
        else
        {
            Console.WriteLine("Tasks:");
            foreach (var task in tasks)
            {
                Console.WriteLine(task);
            }
        }
        Console.ReadKey();
    }

    static void RemoveTask()
    {
        ViewTasks();
        Console.Write("Enter task number to remove: ");
        if (int.TryParse(Console.ReadLine(), out int taskId))
        {
            var taskToRemove = tasks.Find(task => task.Id == taskId);
            if (taskToRemove != null)
            {
                tasks.Remove(taskToRemove);
                Console.WriteLine("Task removed successfully.");
            }
            else
            {
                Console.WriteLine("Task not found.");
            }
        }
        else
        {
            Console.WriteLine("Invalid input.");
        }
        Console.ReadKey();
    }
}

public class Task
{
    public int Id { get; set; }
    public string Description { get; set; }
    public bool IsCompleted { get; set; }

    public Task(int id, string description)
    {
        Id = id;
        Description = description;
        IsCompleted = false;
    }

    public override string ToString()
    {
        return $"{Id}. {Description} - {(IsCompleted ? "Completed" : "Pending")}";
    }
}
