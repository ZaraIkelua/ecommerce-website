pageData = {
    currentPage: 1
}

function readQueryParam(key) {
    // Create URLSearchParams object from the current URL's query string
    const params = new URLSearchParams(window.location.search);

    // Get the value of the specified key
    keyValue = params.get(key);
    return keyValue != null ? keyValue : ''
}

function makePlaceholder() {
    return `
        <div class="card mt-3" aria-hidden="true">
            <div class="img_height bg-secondary my-10"></div>
            <div class="card-body">
                <h5 class="card-title placeholder-glow">
                    <span class="placeholder col-6"></span>
                </h5>
                <p class="card-text placeholder-glow">
                    <span class="placeholder col-7"></span>
                    <span class="placeholder col-4"></span>
                    <span class="placeholder col-4"></span>
                    <span class="placeholder col-6"></span>
                    <span class="placeholder col-8"></span>
                </p>
                <a class="btn btn-primary disabled placeholder col-6" aria-disabled="true"></a>
            </div>
        </div>
    `;
}

function addPlaceholder() {
    let div_el = document.createElement("div");
    div_el.setAttribute("id", "placeholder");
    div_el.setAttribute("class", "row");
    for (let i = 0; i < 5; i++) {
        div_el.innerHTML += makePlaceholder();
    }

    document.getElementById("shop_data").appendChild(div_el);
}

function load_next_data(step=0) {
    addPlaceholder();
    currentPage = pageData.currentPage + step
    fetchData(`/products?search=${readQueryParam('search')}&page=${currentPage+step}`).then(data => {
        let products_data = data.response;
        shop_field = document.getElementById('shop_data');

        if (products_data.length > 0) {
            document.getElementById('placeholder').remove();
        } else if(pageData.currentPage + step == 1) {
            document.getElementById('placeholder').innerHTML = '<h1 class="text-center text-white">No products available</h1>'
            document.getElementById('pagination').remove()
        } else {
            document.getElementById('placeholder').remove()
            document.getElementById('pagination').remove()
        }
        products_data.forEach(product => {
            console.log(products_data)
            next_div = `
            <div class="card mt-3" style="width: 18rem">
                <img src="${product.image}" class="card-img-top" style="height: 10rem;" alt="..." />
                <div class="card-body">
                    <h5 class="card-title">${product.name}</h5>
                    <p class="card-text">
                        <h5>${product.price}</h5>
                        <span>${product.discount}</span>
                        <p>${product.description}</p>
                    </p>
                    <a href="/product/${product.id}" class="btn btn-primary">Know More!</a>
                </div>
            </div>

            `
            shop_field.innerHTML += next_div
        })
        pageData.currentPage = currentPage
    })
    console.log(pageData)
}

window.onload = () => load_next_data();