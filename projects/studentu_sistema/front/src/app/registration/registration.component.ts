import {Component, OnInit} from '@angular/core';
import {User} from '../services/user.model';
import {NgForm} from '@angular/forms';
import {UserService} from '../services/user.service';
import {toast} from 'angular2-materialize';
import {Router} from '@angular/router';
import {FacultiesSubjectsService} from '../services/faculties-subjects.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {
  user = new User(null);
  emailPattern = '^[a-ž0-9._%+-]+@[a-ž0-9.-]+\.[a-ž]{2,4}$';
  listFacultiesAndSubjects;
  universities;
  selectedUniversity;

  constructor(private userService: UserService, private router: Router, private facultiesAndSubjectsService: FacultiesSubjectsService) {
  }

  ngOnInit() {
    this.resetForm();
    this.loadUniversities();
  }

  resetForm(form?: NgForm) {
    if (form != null) {
      form.reset();
    }
    this.user = {
      userName: '',
      password: '',
      email: '',
      firstName: '',
      lastName: '',
      university: '',
    };
  }

  OnSubmit(form: NgForm) {
    this.userService.registerUser(form.value)
      .subscribe((data: any) => {
          if (data.id) {
            this.resetForm(form);
            toast(data.userName + ' registracija sėkminga', '4000');
            this.router.navigate(['/prisijungimas']);
          }
        },
        error => {
          toast(error.error.message, '4000');
        });
  }

  loadUniversities() {
    this.facultiesAndSubjectsService.getAllUniversities()
      .then(data => {
        console.log(data);
        this.listFacultiesAndSubjects = data;
        const temp = [];
        this.listFacultiesAndSubjects.forEach((facultyAndSubject) => temp.push(facultyAndSubject['university']));
        this.universities = Array.from(new Set(temp));
      });
  }

}
