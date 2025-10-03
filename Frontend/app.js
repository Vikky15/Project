function getBaseUrl(service) {
  const hostname = window.location.hostname;
  switch(service) {
    case 'user': return `http://${hostname}:8000`;
    case 'product': return `http://${hostname}:8001`;
    case 'order': return `http://${hostname}:8002`;
  }
}

async function fetchData(service, endpoint) {
  const BASE_URL = getBaseUrl(service);
  try {
    const response = await fetch(`${BASE_URL}${endpoint}`);
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
    const data = await response.json();
    renderTable(data, service);
  } catch (error) {
    console.error('Error fetching data:', error);
    document.getElementById('app').innerHTML = `<p id="error">Error fetching ${service} data</p>`;
  }
}

function getIcon(service) {
  switch(service) {
    case 'user': return '<i class="fas fa-user"></i>';
    case 'product': return '<i class="fas fa-box"></i>';
    case 'order': return '<i class="fas fa-shopping-cart"></i>';
    default: return '';
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

  headingDiv.innerHTML = `<h2>${getIcon(service)} ${service.charAt(0).toUpperCase() + service.slice(1)} Data</h2>`;

  const keys = Object.keys(data[0]);
  let table = '<table><thead><tr>';
  keys.forEach(key => table += `<th>${getIcon(service)} ${key}</th>`);
  table += '</tr></thead><tbody>';

  data.forEach(item => {
    table += '<tr>';
    keys.forEach(key => table += `<td>${item[key]}</td>`);
    table += '</tr>';
  });

  table += '</tbody></table>';
  appDiv.innerHTML = table;
}

document.getElementById('fetchBtn').addEventListener('click', () => {
  const service = document.getElementById('serviceSelect').value;
  const endpoint = service === 'user' ? '/users' :
                   service === 'product' ? '/products' : '/orders';
  fetchData(service, endpoint);
});

