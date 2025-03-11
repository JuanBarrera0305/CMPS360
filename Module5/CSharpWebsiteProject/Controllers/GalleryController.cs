using Microsoft.AspNetCore.Mvc;

namespace CSharpWebsiteProject.Controllers
{
    public class GalleryController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}