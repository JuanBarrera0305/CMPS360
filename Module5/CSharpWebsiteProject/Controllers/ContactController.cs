using Microsoft.AspNetCore.Mvc;
using CSharpWebsiteProject.Models;

namespace CSharpWebsiteProject.Controllers
{
    public class ContactController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Submit(string name, string email, string message)
        {
            ViewBag.Name = name;
            ViewBag.Email = email;
            ViewBag.Message = message;
            return View("Success");
        }
    }
}