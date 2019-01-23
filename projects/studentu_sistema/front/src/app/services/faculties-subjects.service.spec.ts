import { TestBed, inject } from '@angular/core/testing';

import { FacultiesSubjectsService } from './faculties-subjects.service';

describe('FacultiesSubjectsService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [FacultiesSubjectsService]
    });
  });

  it('should be created', inject([FacultiesSubjectsService], (service: FacultiesSubjectsService) => {
    expect(service).toBeTruthy();
  }));
});
