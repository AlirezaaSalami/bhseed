const productFilters = document.querySelectorAll('.filters-title')
const productItems = document.querySelectorAll('.product-item-box')
const productFiltersItems = document.querySelectorAll('.product-filters-item')
const allCompanies = document.querySelector('.companies')
productFilters.forEach(productFilter => {
    productFilter.addEventListener('click', () => {
        productFilters.forEach(productFilter => {
            productFilter.classList.remove('active')
        })
        productFilter.classList.add('active')
        if (!productFilter.classList.contains('companies')) {
            productFilter.nextElementSibling.classList.toggle('hidden')
        }
    })
})

productFiltersItems.forEach(productFiltersItem => {
    productFiltersItem.addEventListener('click', () => {
        productItems.forEach(productIteme => {
            if (!productIteme.dataset.itemattr.includes(productFiltersItem.dataset.filter)) {
                productIteme.classList.add('hidden')
            } else {
                productIteme.classList.remove('hidden')
            }
        })
    })
})

function allCompaniesFilter() {
    productItems.forEach(productIteme => {
        if (!productIteme.dataset.itemattr.includes(allCompanies.dataset.filter)) {
            productIteme.classList.add('hidden')
        } else {
            productIteme.classList.remove('hidden')
        }
    })
}
allCompaniesFilter()
allCompanies.addEventListener('click', allCompaniesFilter)