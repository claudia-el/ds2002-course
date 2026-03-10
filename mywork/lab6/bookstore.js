// Task 2: use database
use bookstore

// Task 3: insert first author
db.authors.insertOne({
  "name": "Jane Austen",
  "nationality": "British",
  "bio": {
    "short": "English novelist known for novels about the British landed gentry.",
    "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development."
  }
})

// Task 4: update to add birthday
db.authors.updateOne(
  { name: "Jane Austen" },
  { $set: { birthday: "1775-12-16" } }
)

// Task 5: insert four more authors
db.authors.insertMany([
  {
    name: "Leo Tolstoy",
    nationality: "Russian",
    bio: {
      short: "Famous Russian novelist",
      long: "Leo Tolstoy wrote novels like 'War and Peace' and 'Anna Karenina'."
    },
    birthday: "1828-09-09"
  },
  {
    name: "Dante Alighieri",
    nationality: "Italian",
    bio: {
      short: "Famous Italian poet",
      long: "Dante Alighieri wrote 'The Divine Comedy', one of the greatest works of literature."
    },
    birthday: "1265-05-29"
  },
  {
    name: "Homer",
    nationality: "Greek",
    bio: {
      short: "Ancient Greek poet",
      long: "Homer is the author of the epics 'The Iliad' and 'The Odyssey'."
    },
    birthday: "-800-01-01"
  },
  {
    name: "Haruki Murakami",
    nationality: "Japanese",
    bio: {
      short: "Famous Japanese novelist",
      long: "Writes magical stories."
    },
    birthday: "1949-01-12"
  }
])


// Task 6: total count
db.authors.countDocuments()

// Task 7: British authors, sorted by name
db.authors.find({ nationality: "British" }).sort({ name: 1 })