##Models

###Genre
- pk: Primary key
- title: String, unique, index, not null
- description: Text, unique, nullable


###Books
- pk: Primary key
- title: String, index, not null
- description: Text
- book<->genre one-to-one
- book<->users one-to-many
- book<->author one-to-one


###Author
- pk: Primary key
- first_name: String, not null
- last_name: String, index, not null
- author<->books one-to-many
