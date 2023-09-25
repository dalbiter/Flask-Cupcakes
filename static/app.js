
const BASE_URL = "/api/cupcakes"
const $ul = $('#cupcakes-list');

async function getCupcakes() {
    const resp = await axios.get(BASE_URL);
    cupcakes = resp.data.cupcakes;
    for(let cupcake of cupcakes){
        let newcupcake = $(createCupcakeLi(cupcake))
        $ul.append(newcupcake)   
    };
};

getCupcakes();

function createCupcakeLi(cupcake){ 
    const $newli = $(`<li class="mb-3"><br><b>Flavor:</b> ${cupcake.flavor} <br> <b>Size:</b> ${cupcake.size} <br> <b>Rating:</b> ${cupcake.rating}</li>`)
    const $cupcakeImg = $(`<img src="${cupcake.image}" height="60px" width="60px"></img>`)
    $newli.prepend($cupcakeImg).appendTo($ul)
};

$('#cupcake-form').on("submit", async function (e) {
    e.preventDefault();

    let $flavor = $('#flavor').val();
    let $size = $('#size').val();
    let $rating = $('#rating').val();
    let $image = $('#image').val();
    let newCupcake = {
        flavor: $flavor,
        size: $size,
        rating: $rating,
        image: $image
    };
    await axios.post(BASE_URL, data=newCupcake);
    let $newCupcake = createCupcakeLi(newCupcake);
    $ul.append($newCupcake); 
    $('#cupcake-form').trigger("reset")
});





