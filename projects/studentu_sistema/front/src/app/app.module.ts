import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {AppRoutingModule} from './app-routing.module';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {HashLocationStrategy, LocationStrategy} from '@angular/common';
import {MaterializeModule} from 'angular2-materialize';
import {Ng2SearchPipeModule} from 'ng2-search-filter';

import {FacultiesSubjectsService} from './services/faculties-subjects.service';
import {UploadService} from './services/upload.service';
import {UserService} from './services/user.service';
import {ProfileService} from './services/profile.service';
import {GuardService} from './services/guard.service';

import {AppComponent} from './app.component';
import {FileHandlerComponent} from './file-handler/file-handler.component';
import {RegistrationComponent} from './registration/registration.component';
import {LoginComponent} from './login/login.component';
import {ProfileComponent} from './profile/profile.component';
import { InterceptorComponent } from './-interceptor/-interceptor.component';



@NgModule({
  declarations: [
    AppComponent,
    FileHandlerComponent,
    RegistrationComponent,
    LoginComponent,
    ProfileComponent,
    InterceptorComponent,
  ],
  imports: [
    MaterializeModule,
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    Ng2SearchPipeModule
  ],
  providers: [
    // {
    //   provide: HTTP_INTERCEPTORS,
    //   useClass: InterceptorComponent,
    //   multi: true
    // },
    GuardService,
    {
    provide: LocationStrategy,
    useClass: HashLocationStrategy
  }, FacultiesSubjectsService, UploadService, UserService, ProfileService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
