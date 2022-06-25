ALTER TABLE products
add constraint fk_products_categories
foreign key (category_id) references categories (id);