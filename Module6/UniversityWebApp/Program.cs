var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();
builder.Services.AddHttpClient();  // Add HttpClient for API communication
builder.Services.AddSingleton<UniversityService>();  // Register the UniversityService

// Add CORS policy to allow any origin, method, and header (adjust as needed)
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
    {
        policy.AllowAnyOrigin().AllowAnyMethod().AllowAnyHeader();
    });
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseDeveloperExceptionPage(); // Optional for dev mode
}
else
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts(); // Secure HTTP Strict Transport Security (HSTS)
}

app.UseHttpsRedirection();
app.UseStaticFiles(); // Make sure static files can be accessed

// Use CORS policy here
app.UseCors("AllowAll"); // Enable CORS globally for all routes

app.UseRouting();
app.UseAuthorization();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

// Run the app
app.Run();