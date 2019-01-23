import {Component, OnInit} from '@angular/core';
import {User} from '../services/user.model';
import {NgForm} from '@angular/forms';
import {UserService} from '../services/user.service';
import {Router} from '@angular/router';
import {toast} from 'angular2-materialize';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  user = new User(null);

  constructor(private userService: UserService, private router: Router) {
    userService.logoutUser();
  }

  ngOnInit() {
  }

  resetForm(form?: NgForm) {
    if (form != null) {
      form.reset();
    }
    this.user.password = '';
  }

  OnSubmit(form: NgForm) {
    this.userService.loginUser(form.value)
      .subscribe(data => {
        if (data.length === 16) { // access token 16 characters
          toast('Prisijungta sėkmingai', '4000');
          this.resetForm(form);
          this.router.navigate(['/duomenys']);
        } else {
          toast(data, '4000');
        }
      });
  }

}
