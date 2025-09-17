// API URL for the backend
const API_URL = 'http://127.0.0.1:5000/api/covid-data';

// Get DOM elements
const countrySelect = document.getElementById('country-select');
const statusMessage = document.getElementById('status-message');
const totalTrialsEl = document.getElementById('total-trials');
const topCountriesCard = document.getElementById('top-countries-card');

// Global chart instances
let statusChart, countriesChart, phaseChart, trialsOverTimeChart;
let allData = {};

// Helper function to show messages
const showStatus = (message, isError = false) => {
    statusMessage.textContent = message;
    statusMessage.className = `text-sm text-center ${isError ? 'text-red-400' : 'text-gray-400'}`;
};

// Function to fetch data from the backend
const fetchData = async () => {
    showStatus('Loading data...');
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            console.error('HTTP Status:', response.status, response.statusText);
            throw new Error('Network response was not ok');
        }
        allData = await response.json();
        renderDashboard();
        showStatus('Data loaded successfully.');
    } catch (error) {
        console.error('Fetch error:', error);
        showStatus('Failed to load data. Please check if the backend is running.', true);
    }
};

// Function to populate the country dropdown
const populateCountrySelector = () => {
    // Clear existing options
    countrySelect.innerHTML = '<option value="Global">Global</option>';
    const countries = Object.keys(allData).filter(country => country !== 'Global');
    countries.forEach(country => {
        const option = document.createElement('option');
        option.value = country;
        option.textContent = country;
        countrySelect.appendChild(option);
    });
};

// Function to update all charts with data for the selected country
const updateCharts = (data) => {
    // Update total trials
    totalTrialsEl.textContent = data.totalTrials.toLocaleString();

    // Render Trial Status Distribution Chart (Doughnut)
    if (statusChart) statusChart.destroy();
    const statusLabels = Object.keys(data.trialStatusDistribution);
    const statusValues = Object.values(data.trialStatusDistribution);
    statusChart = new Chart(document.getElementById('statusChart').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: statusLabels,
            datasets: [{
                data: statusValues,
                backgroundColor: ['#3b82f6', '#10b981', '#f59e0b', '#ef4444'],
                borderColor: '#2d3748',
                borderWidth: 2,
            }],
        },
        options: {
            responsive: true,
            plugins: {
                legend: { labels: { color: '#e2e8f0' } },
                tooltip: { backgroundColor: 'rgba(45, 55, 72, 0.9)' }
            },
        }
    });

    // Render Top Countries Chart (Bar) - only for Global view
    if (countriesChart) countriesChart.destroy();
    if (data.name === 'Global') {
        topCountriesCard.style.display = 'block';
        const countryLabels = data.topCountries.map(c => c.country);
        const countryValues = data.topCountries.map(c => c.count);
        countriesChart = new Chart(document.getElementById('countriesChart').getContext('2d'), {
            type: 'bar',
            data: {
                labels: countryLabels,
                datasets: [{
                    label: 'Trials',
                    data: countryValues,
                    backgroundColor: '#38bdf8',
                    borderRadius: 6,
                }],
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true, grid: { color: 'rgba(255,255,255,0.1)' }, ticks: { color: '#e2e8f0' } },
                    x: { grid: { color: 'rgba(255,255,255,0.1)' }, ticks: { color: '#e2e8f0' } },
                },
                plugins: {
                    legend: { display: false },
                    tooltip: { backgroundColor: 'rgba(45, 55, 72, 0.9)' }
                },
            }
        });
    } else {
        topCountriesCard.style.display = 'none';
    }

    // Render Phase Status Distribution Chart (Stacked Bar)
    if (phaseChart) phaseChart.destroy();
    const phaseLabels = data.phaseStatusDistribution.map(p => p.phase);
    const recruitingData = data.phaseStatusDistribution.map(p => p.Recruiting);
    const completedData = data.phaseStatusDistribution.map(p => p.Completed);
    const activeData = data.phaseStatusDistribution.map(p => p['Active']);
    phaseChart = new Chart(document.getElementById('phaseChart').getContext('2d'), {
        type: 'bar',
        data: {
            labels: phaseLabels,
            datasets: [
                { label: 'Recruiting', data: recruitingData, backgroundColor: '#4ade80' },
                { label: 'Completed', data: completedData, backgroundColor: '#fbbf24' },
                { label: 'Active', data: activeData, backgroundColor: '#60a5fa' },
            ]
        },
        options: {
            responsive: true,
            scales: {
                x: { stacked: true, grid: { color: 'rgba(255,255,255,0.1)' }, ticks: { color: '#e2e8f0' } },
                y: { stacked: true, beginAtZero: true, grid: { color: 'rgba(255,255,255,0.1)' }, ticks: { color: '#e2e8f0' } }
            },
            plugins: { legend: { labels: { color: '#e2e8f0' } } }
        }
    });

    // Render Trials Over Time Chart (Line)
    if (trialsOverTimeChart) trialsOverTimeChart.destroy();
    const timeLabels = data.trialsOverTime.map(t => t.date);
    const timeCounts = data.trialsOverTime.map(t => t.count);
    trialsOverTimeChart = new Chart(document.getElementById('trialsOverTimeChart').getContext('2d'), {
        type: 'line',
        data: {
            labels: timeLabels,
            datasets: [{
                label: 'New Trials',
                data: timeCounts,
                borderColor: '#ef4444',
                backgroundColor: 'rgba(239, 68, 68, 0.2)',
                borderWidth: 2,
                tension: 0.4,
                fill: true,
            }],
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true, grid: { color: 'rgba(255,255,255,0.1)' }, ticks: { color: '#e2e8f0' } },
                x: { grid: { color: 'rgba(255,255,255,0.1)' }, ticks: { color: '#e2e8f0' } },
            },
            plugins: { legend: { labels: { color: '#e2e8f0' } } },
        }
    });
};

// Main rendering function
const renderDashboard = () => {
    populateCountrySelector();
    updateCharts(allData['Global']);
};

// Event listener for country selection change
countrySelect.addEventListener('change', (event) => {
    const selectedCountry = event.target.value;
    if (allData[selectedCountry]) {
        updateCharts(allData[selectedCountry]);
    }
});

// Initialize the dashboard on page load
document.addEventListener('DOMContentLoaded', fetchData);
