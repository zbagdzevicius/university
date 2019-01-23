import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';

@Injectable()
export class ProfileService {

  constructor(private http: HttpClient) {
  }

  listFiles(): Observable<any> {
    const userName = sessionStorage.getItem('userName');
    const formdata: FormData = new FormData();

    formdata.append('userName', userName);
    return this.http.post('/file/get/userFiles', formdata);
  }

  deleteFile(fileName) {
    const userName = sessionStorage.getItem('accessToken');
    const formdata: FormData = new FormData();

    formdata.append('userName', userName);
    this.http.post('/file/delete/file/' + fileName, formdata);
  }

}
