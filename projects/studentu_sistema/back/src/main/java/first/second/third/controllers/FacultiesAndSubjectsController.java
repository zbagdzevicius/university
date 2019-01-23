package first.second.third.controllers;


import first.second.third.beans.documents.FacultiesAndSubjects;
import first.second.third.beans.response.FacultiesAndSubjectsResponse;
import first.second.third.beans.response.UniversityResponse;
import first.second.third.services.FacultiesAndSubjectsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping(value = "/facultiesAndSubjects")
@CrossOrigin
public class FacultiesAndSubjectsController {

    @Autowired
    private FacultiesAndSubjectsService service;

    @GetMapping
    public List<FacultiesAndSubjectsResponse> getAllFacultiesAndSubjects() {
        return service.getAllFacultiesAndSubjects();
    }

    @GetMapping("/universities")
    public  List<UniversityResponse> getAllUniversities(){
        return service.getAllUniversities();
    }

    @PostMapping
    public FacultiesAndSubjectsResponse addPost(@Valid @RequestBody FacultiesAndSubjects facultiesAndSubjects) {
        return new FacultiesAndSubjectsResponse(service.addNewFacultiesAndSubjects(facultiesAndSubjects));
    }

    @PostMapping("/multiple")
    public Boolean addPostMultiple(@RequestBody FacultiesAndSubjects[] facultiesAndSubjects){
        for (FacultiesAndSubjects faculty : facultiesAndSubjects){
            this.addPost(faculty);
        }
        return true;
    }

    @DeleteMapping("/{id}")
    public void removePost(@PathVariable("id") String id) {
        service.deleteFacultiesAndSubjects(id);
    }

    @DeleteMapping
    public void deleteAll(){service.deleteAllFacultiesAndSubjects();}



}
