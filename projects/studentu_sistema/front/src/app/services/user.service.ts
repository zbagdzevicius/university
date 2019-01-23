import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import 'rxjs/add/operator/map';
import {User} from './user.model';
import {Router} from '@angular/router';

@Injectable()
export class UserService {
  university: String;

  constructor(private http: HttpClient, private router: Router) {
  }

  registerUser(user: User) {
    const body: User = {
      userName: user.userName,
      password: user.password,
      email: user.email,
      firstName: user.firstName,
      lastName: user.lastName,
      university: user.university,
    };
    return this.http.post('/user/register', body);
  }

  loginUser(user: User) {
    const formdata: FormData = new FormData();
    formdata.append('userName', user.userName);
    formdata.append('password', user.password);
    return this.http.post('/user/login', formdata, {
      responseType: 'text'
    })
      .map(data => { // login successful if there's a token in the response
        if (data) {
          sessionStorage.setItem('userName', user.userName);
          sessionStorage.setItem('accessToken', data); // store token in local storage to keep user logged in between page refreshes;
        }
        return data;
      });
  }

  logoutUser() {
    // remove user from local storage to log user out
    sessionStorage.clear();
    this.router.navigate(['/#/prisijungimas']);
  }

  authUser() {
    const accessToken = sessionStorage.getItem('accessToken');
    const formdata: FormData = new FormData();
    formdata.append('accessToken', accessToken);
    if (accessToken != null) {
      return this.http.post('/user/auth', formdata)
        .map(data => {
          return data;
        });
    }
  }

  getUserUniversity() {
    const formdata: FormData = new FormData();
    formdata.append('userName', 'as');
    console.log('wp');
    return this.http.post('/user/university', formdata)
      .map(data => {
        console.log('wpaeawf');
      });
  }
}
