import {Injectable} from '@angular/core';
import {HttpClient, HttpEvent, HttpRequest} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';

@Injectable()
export class UploadService {

  constructor(private http: HttpClient) {
  }

  listFiles(subject): Observable<any> {
    const formdata: FormData = new FormData();

    formdata.append('subject', subject);

    return this.http.post('/file', formdata)
      .map(res => {
        return res;
      });
  }

  uploadFile(file: File, faculty, subject) {
    const formdata: FormData = new FormData();

    formdata.append('file', file);
    formdata.append('username', sessionStorage.getItem('userName'));
    formdata.append('faculty', faculty);
    formdata.append('subject', subject);

    const req = new HttpRequest('POST', '/file/upload', formdata, {
      reportProgress: true,
      responseType: 'text'
    });

    return this.http.request(req);
  }

}
