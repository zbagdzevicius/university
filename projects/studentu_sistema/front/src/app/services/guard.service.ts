import {Injectable} from '@angular/core';
import {CanActivate, Router} from '@angular/router';
import {UserService} from './user.service';

@Injectable()
export class GuardService implements CanActivate {

  constructor(public router: Router, public service: UserService) {
  }

  canActivate(): boolean {
    if (!this.service.authUser()) {
      this.router.navigate(['login']);
      return false;
    }
    return true;
  }
}
