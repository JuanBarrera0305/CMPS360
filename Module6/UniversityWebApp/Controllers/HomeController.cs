using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using UniversityWebApp.Models;

namespace UniversityWebApp.Controllers;

public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;
    private readonly UniversityService _universityService;

    // Constructor that accepts both logger and university service
    public HomeController(ILogger<HomeController> logger, UniversityService universityService)
    {
        _logger = logger;
        _universityService = universityService;
    }

    // Index method that retrieves universities from the service
    public async Task<IActionResult> Index()
    {
        var universities = await _universityService.GetUniversitiesAsync();
        return View(universities);  // Pass the universities list to the view
    }

    // New action method for "How Ranking Works" page
    public IActionResult Ranking()
    {
        return View();
    }

    // New action method for "Application Tips" page
    public IActionResult Tips()
    {
        return View();
    }

    // New action method for "Apply Here" page
    public IActionResult Apply()
    {
        return View();
    }

    // Error handling
    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
    public IActionResult Tips()
{
    return View();
}
}