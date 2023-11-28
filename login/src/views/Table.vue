<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Books</h1>
        <hr><br><br>
        <alert :message="message" v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" @click="toggleAddBookModal">
          Add Book
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm" @click='handleDeleteBook(book)'>Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div ref="addBookModal" class="modal fade" :class="{ show: activeAddBookModal, 'd-block': activeAddBookModal }"
      tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add a new book</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close" @click="toggleAddBookModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="addBookTitle" class="form-label">Title:</label>
                <input type="text" class="form-control" id="addBookTitle" v-model="addBookForm.title"
                  placeholder="Enter title">
              </div>
              <div class="mb-3">
                <label for="addBookAuthor" class="form-label">Author:</label>
                <input type="text" class="form-control" id="addBookAuthor" v-model="addBookForm.author"
                  placeholder="Enter author">
              </div>
              <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" id="addBookRead" v-model="addBookForm.read">
                <label class="form-check-label" for="addBookRead">Read?</label>
              </div>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-primary btn-sm" @click="handleAddSubmit">
                  Submit
                </button>
                <button type="button" class="btn btn-danger btn-sm" @click="handleAddReset">
                  Reset
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeAddBookModal" class="modal-backdrop fade show"></div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from '../components/Alert.vue'


export default {
  data() {
    return {
      activeAddBookModal: false,
      addBookForm: {
        title: '',
        author: '',
        read: [],
      },
      books: [],
      message: '',
      showMessage: false,
    };
  },

  components: {
    alert: Alert,
  },
  methods: {
    addBook(payload) {
      const path = 'http://localhost:5000/books';
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book added!';
          this.showMessage = true;
        })
        .catch((error) => {

          console.log(error);
          this.getBooks();
        });
    },
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {

          console.error(error);
        });
    },
    handleAddReset() {
      this.initForm();
    },
    handleAddSubmit() {
      this.toggleAddBookModal();
      let read = false;
      if (this.addBookForm.read[0]) {
        read = true;
      }
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read, // property shorthand
      };
      this.addBook(payload);
      this.initForm();
    },
    initForm() {
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.read = [];
    },
    toggleAddBookModal() {
      const body = document.querySelector('body');
      this.activeAddBookModal = !this.activeAddBookModal;
      if (this.activeAddBookModal) {
        body.classList.add('modal-open');
      } else {
        body.classList.remove('modal-open');
      }
    },
    handleDeleteBook(book) {
      this.removeBook(book.title);
    },
    removeBook(title) {
      const path = `http://localhost:5000/books/${title}`;
      axios.delete(path)
        .then(() => {
          this.getBooks();
          this.message = 'Book removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getBooks();
        });
    },
    updateBook(originalTitle, newBookData) {
      axios.put(`http://127.0.0.1:5000/books/${originalTitle}`, newBookData)
        .then(response => {
          // Actualizar la lista de libros en el frontend
          this.getBooks();
        })
        .catch(error => {
          console.error(error);
        });
    },

  },
  created() {
    this.getBooks();
  },
};
</script>