import { NgModule } from '@angular/core';
import { Routes, RouterModule, CanActivate} from '@angular/router';
import { FileHandlerComponent } from './file-handler/file-handler.component';
import { RegistrationComponent } from './registration/registration.component';
import { LoginComponent } from './login/login.component';
import { ProfileComponent } from './profile/profile.component';
import {GuardService as AuthGuard} from './services/guard.service';

const routes: Routes = [
  {path: 'prisijungimas', component: LoginComponent},
  {path: 'duomenys', component: FileHandlerComponent, canActivate: [AuthGuard]},
  {path: 'registracija', component: RegistrationComponent},
  {path: 'profilis', component: ProfileComponent, canActivate: [AuthGuard]},
  {path: '', redirectTo: 'prisijungimas', pathMatch: 'full'},
  { path: '**', redirectTo: 'prisijungimas' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
