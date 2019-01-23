import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable()
export class FacultiesSubjectsService {
  changeScrollValue = true;

  constructor(private http: HttpClient) { }

  getAllFacultiesAndSubjects() {
    return this.http
      .get('/facultiesAndSubjects', {headers: {'Content-Type' : 'charset=UTF-8'}})
      .toPromise();
  }

  getAllUniversities() {
    return this.http
      .get('/facultiesAndSubjects/universities', {headers: {'Content-Type' : 'charset=UTF-8'}})
      .toPromise();
  }


}
