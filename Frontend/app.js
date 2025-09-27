function getBaseUrl(service) {
  if (window.location.hostname === 'localhost') {
    switch(service) {
      case 'user': return 'http://localhost:8000';
      case 'product': return 'http://localhost:8001';
      case 'order': return 'http://localhost:8002';
    }
  } else {
    switch(service) {
      case 'user': return 'http://user-service:8000';
      case 'product': return 'http://product-service:8000';
      case 'order': return 'http://order-service:8000';
    }
  }
}

async function fetchData(service, endpoint) {
  const BASE_URL = getBaseUrl(service);
  try {
    const response = await fetch(`${BASE_URL}${endpoint}`);
    const data = await response.json();
    console.log(`${service} data:`, data);
    renderTable(data, service);
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    document.getElementById('app').innerHTML = `<p>Error fetching ${service} data</p>`;
  }
}

function renderTable(data, service) {
  const appDiv = document.getElementById('app');
  const headingDiv = document.getElementById('tableHeading');

  if (!data || data.length === 0) {
    headingDiv.innerHTML = '';
    appDiv.innerHTML = '<p>No data available</p>';
    return;
  }

  // Add heading
  headingDiv.innerHTML = `<h2>${service.charAt(0).toUpperCase() + service.slice(1)} Data</h2>`;

  // Create table
  const keys = Object.keys(data[0]);
  let table = '<table><thead><tr>';
  keys.forEach(key => table += `<th>${key}</th>`);
  table += '</tr></thead><tbody>';

  data.forEach(item => {
    table += '<tr>';
    keys.forEach(key => table += `<td>${item[key]}</td>`);
    table += '</tr>';
  });

  table += '</tbody></table>';
  appDiv.innerHTML = table;
}

document.getElementById('fetchBtn').addEventListener('click', async () => {
  const service = document.getElementById('serviceSelect').value;
  const endpoint = service === 'user' ? '/users' :
                   service === 'product' ? '/products' : '/orders';
  await fetchData(service, endpoint);
});

