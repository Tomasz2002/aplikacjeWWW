## 1. Pobranie wszystkich kategorii
query {
  allCategories {
    id
    name
    description
  }
}

## Wyszukiwanie postów po fragmencie tytułu
query {
  postsByTitleSearch(search: "tytul") {
    id
    title
    text
    createdAt
  }
}
## Liczba postów użytkownika
query {
  countPostsByUser(userId: 1)
}

## Posty dla danego Tematu
query {
  postsByTopic(topicId: 1) {
    id
    title
    createdBy {
      username
    }
  }
}
## Mutacja: Tworzenie posta
mutation {
  createPost(
    title: "Post z GraphQL", 
    text: "Treść posta utworzona przez mutację", 
    slug: "post-z-graphql", 
    topicId: 1, 
    userId: 1
  ) {
    post {
      id
      title
      slug
    }
  }
}
## Mutacja: Aktualizacja posta
mutation {
  updatePost(id: 1, title: "Zaktualizowany tytuł") {
    post {
      id
      title
      text
    }
  }
}
## Mutacja: Usuwanie posta
mutation {
  deletePost(id: 1) {
    message
  }
}