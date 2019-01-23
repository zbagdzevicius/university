import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FileHandlerComponent } from './file-handler.component';

describe('FileHandlerComponent', () => {
  let component: FileHandlerComponent;
  let fixture: ComponentFixture<FileHandlerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FileHandlerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FileHandlerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
