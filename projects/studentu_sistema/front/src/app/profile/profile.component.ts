import {Component, OnInit} from '@angular/core';
import {ProfileService} from '../services/profile.service';
import {Observable} from 'rxjs/Observable';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  fileUploads: Observable<string[]>;
  term = '';

  constructor(private profileService: ProfileService) {
  }


  ngOnInit() {
    this.showFiles();
  }

  showFiles() {
    this.fileUploads = this.profileService.listFiles();
  }

  deleteFile(fileName) {
    this.profileService.deleteFile(fileName);
    setTimeout(this.showFiles(), '3000');
  }
}
