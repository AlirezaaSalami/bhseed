const productFilters = document.querySelectorAll('.filters-title')
const productItems = document.querySelectorAll('.product-item')
const productFiltersItems = document.querySelectorAll('.product-filters-item')
productFilters.forEach(productFilter => {
    productFilter.addEventListener('click', () => {
        productFilters.forEach(productFilter => {
            productFilter.classList.remove('active')
        })
        productFilter.classList.add('active')
        if(!productFilter.classList.contains('all-filters')){
            productFilter.nextElementSibling.classList.toggle('hidden')
        }
        productItems.forEach(productItem => {
            if (productFilter.dataset.filter == 'all') {
                productItem.classList.remove('hidden')
            }
        })

    })
})

productFiltersItems.forEach(productFiltersItem => {
    productFiltersItem.addEventListener('click', () => {
        productItems.forEach(productIteme => {
            if (!productIteme.dataset.itemattr.includes(productFiltersItem.dataset.filter)) {
                productIteme.classList.add('hidden')
            }else {
                productIteme.classList.remove('hidden')
            }
        })
    })
})