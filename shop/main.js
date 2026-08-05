import ITEMS from "../data/TacoShop/Inventory.json" with { type: "json"}


function printItems(){
    const items = ITEMS["items"]
    const container = document.getElementById("shop")

    // Create the dom elements
    items.forEach((item) => {
        console.log(item["name"])
        const div = document.createElement("div")
        div.innerHTML = `
            <strong>${item["name"]}</strong>
            <p>Precio: $${item["price"]}</p>
            <img src=${item["image_url"]} width="100"/>
            <p>Quedan disponibles: ${item["quantity"]}</p>
            <a href="https://api.whatsapp.com/send?phone=5584673119&text=Hola%2C%20V%C3%AD%20el%20beyble%20${item["name"]}%20por%20$${item["price"]}%20y%20quiero%20comprarlo" target="_blank">Envíar mensaje para comprar este beyblade</a>
            <hr>
            `;
        container.appendChild(div)
    })
}

printItems()