using Microsoft.AspNetCore.Mvc;

namespace CSharpWebsiteProject.Controllers
{
    public class ConditionalController : Controller
    {
        public IActionResult Index()
        {
            ViewBag.TimeOfDayMessage = GetTimeOfDayMessage();
            return View();
        }

        public IActionResult CheckNumber(int number)
        {
            string result = number % 2 == 0 ? "Even" : "Odd";
            ViewBag.Number = number;
            ViewBag.Result = result;
            return View();
        }

        private string GetTimeOfDayMessage()
        {
            int hour = DateTime.Now.Hour;
            if (hour < 12)
                return "Good morning!";
            else if (hour < 18)
                return "Good afternoon!";
            else
                return "Good evening!";
        }
    }
}