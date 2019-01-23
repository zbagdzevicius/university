import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {UploadService} from '../services/upload.service';
import {HttpEventType, HttpResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import {toast} from 'angular2-materialize';
import {UserService} from '../services/user.service';
import {Router} from '@angular/router';
import {FacultiesSubjectsService} from '../services/faculties-subjects.service';
import {ProfileService} from '../services/profile.service';

@Component({
  selector: 'app-file-handler',
  templateUrl: './file-handler.component.html',
  styleUrls: ['./file-handler.component.css']
})
export class FileHandlerComponent implements OnInit {
  listFacultiesAndSubjects;
  faculties;
  selectedFaculty;
  selectedSubject;
  subjectsBySelectedFaculty = [];
  filename: string;

  uploadButtonShow = false;
  progressBar = false; // hide progress bar
  selectedFiles: FileList; // show selected files
  currentFileUpload: File; // files to upload
  progress: { percentage: number } = {percentage: 0}; // track uploading process
  showFile = false; // show file list
  fileUploads: Observable<string[]>;
  @Output()
  newFile = new EventEmitter<Object>();
  term = '';

  constructor(
    private uploadService: UploadService,
    private userService: UserService,
    private router: Router,
    public facultiesAndSubjectsService: FacultiesSubjectsService,
    private profileService: ProfileService) {
  }

  ngOnInit() {
    this.loadFacultiesAndSubjects(); // load faculties and subjects
    toast('Pasirinkite fakultetą bei studijų dalyką', '4000');
  }

  selectFile(event) {
    this.selectedFiles = event.target.files;
  }

  uploadButtonShowSwitch() {
    this.uploadButtonShow = true;
    toast('Dėmesio!<br>Maksimalus failo dydis 16 MB', '4000');
  }

  showFiles(enable: boolean, subject) {
    this.showFile = enable;

    if (enable) {
      this.fileUploads = this.uploadService.listFiles(subject);
    }
  }


  // choices
  getSubjectsByFaculty(faculty) {
    if (this.facultiesAndSubjectsService.changeScrollValue) {
      this.selectedSubject = '';
    } else {
      this.facultiesAndSubjectsService.changeScrollValue = true;
    }
    if (this.listFacultiesAndSubjects != null) {
      this.listFacultiesAndSubjects.forEach(data => {
        console.log(data);
        if (data['faculty'] === faculty) {
          this.subjectsBySelectedFaculty.push(data['subject']);
        }
      });
    }
  }

  loadFacultiesAndSubjects() {
    this.facultiesAndSubjectsService.getAllFacultiesAndSubjects()
      .then(data => {
        this.listFacultiesAndSubjects = data;
        const temp = [];
        this.listFacultiesAndSubjects.forEach((data) => temp.push(data['faculty']));
        this.faculties = Array.from(new Set(temp));
      });
  }

  uploadFile(faculty, subject) {
    this.progressBar = true;
    this.progress.percentage = 0;

    this.currentFileUpload = this.selectedFiles.item(0);
    this.uploadService.uploadFile(this.currentFileUpload, faculty, subject).subscribe(event => {
      if (event.type === HttpEventType.UploadProgress) {
        this.progress.percentage = Math.round(100 * event.loaded / event.total);
      } else if (event instanceof HttpResponse) {
        toast(event.body, '4000');
      } else if (!this.selectedFiles.item(0)) {
        toast('Pasirinkite failą!', '4000');
      }
    }, error => {
      toast('Failo dydis viršija maksimalų 16 MB limitą', '4000');
    });
    this.progressBar = false;
  }

  deleteFile(fileName) {
    this.profileService.deleteFile(fileName);
    // setTimeout(this.showFiles(), '3000');
  }
}
