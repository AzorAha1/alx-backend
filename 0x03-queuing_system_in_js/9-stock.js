const express = require('express');
const { createClient } = require('redis');
const { promisify } = require('util');


const client = createClient();
client.on('error', (err) => console.log('Redis Client Error', err));

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);
const app = express();
const port = 1245;

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Function to get item by ID
function getItemById(id) {
  return listProducts.find(item => item.itemId === id);
}
async function reserveStockById(itemId, stock) {
    await setAsync(`item.${itemId}`, stock);
  }

// Function to get the current reserved stock by item ID
async function getCurrentReservedStockById(itemId) {
  const thestock = await getAsync(`${itemId}`);
  return thestock
}



app.get('/list_products', (req, res) => {
  res.json(listProducts);
});
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  res.json({ ...product, currentQuantity: currentStock !== null ? currentStock : product.initialAvailableQuantity });
});
// Create the route GET /reserve_product/:itemId
app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId, 10);
    const product = getItemById(itemId);
  
    if (!product) {
      return res.status(404).json({ status: 'Product not found' });
    }
    const currentStock = await getCurrentReservedStockById(itemId);
    const stocktouse = currentStock !== null ? currentStock : product.initialAvailableQuantity;
    if (stocktouse <= 0) {
        return res.json({ status: 'Not enough stock available', itemId });
    }
    await reserveStockById(itemId, stocktouse - 1);
    res.json({ status: 'Reservation confirmed', itemId });
})
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
