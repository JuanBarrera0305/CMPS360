using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;
using System.Collections.Generic;

public class UniversityService
{
    private readonly HttpClient _httpClient;

    // Constructor to inject HttpClient
    public UniversityService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    // Method to get universities from the API
    public async Task<List<University>> GetUniversitiesAsync()
    {
        // Change the URL to match the correct port (5001 or 5224)
        var response = await _httpClient.GetStringAsync("http://localhost:5001/api/universities");  // This should be the API's correct URL
        return JsonConvert.DeserializeObject<List<University>>(response); // Deserialize the JSON response into a List of University objects
    }
}

// Model for University (assumed structure)
public class University
{
    public int Id { get; set; }
    
    // Make Name and Location nullable to avoid the warning
    public string? Name { get; set; }
    public string? Location { get; set; }
    
    public int Ranking { get; set; }
}