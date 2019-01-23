package first.second.third.controllers;

import first.second.third.beans.documents.Datafiles;
import first.second.third.beans.response.FilenamesResponse;
import first.second.third.services.DatafilesService;
import org.json.HTTP;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletResponse;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.InputStream;
import java.util.List;

@RestController
@RequestMapping(value = "/file")
@CrossOrigin
public class DatafilesController {

    @Autowired
    private DatafilesService datafilesService;

    @PostMapping
    public List<FilenamesResponse> getFilenamesBySubject(@RequestParam("subject") String subject){
        return datafilesService.getFilesFilenames(subject);
    }

    @PostMapping("/upload")
    public String fileUpload(@RequestParam("file") MultipartFile multipart,
                             @RequestParam("username") String username,
                             @RequestParam("faculty") String faculty,
                             @RequestParam("subject") String subject) {
        try{
            return datafilesService.fileUpload(multipart, username, faculty, subject);
        } catch (Exception e){
            return e.toString();
        }
    }

    @PostMapping("/get/userFiles")
    public List<FilenamesResponse> getFilenamesByUserName(@RequestParam("userName") String userName){
        return datafilesService.getFilesFilenamesByUserName(userName);
    }

    @GetMapping("/get/{fileName:.+}")
    public void retrieveFile(@PathVariable String fileName,
                             HttpServletResponse response){
    try {
        Datafiles datafile = datafilesService.getDatafileGetByFilename(fileName);
        byte[] dataFileInByte = datafile.getFile().getData();
        InputStream fileStream = new ByteArrayInputStream(dataFileInByte);
        response.setContentType(datafile.getContentType());
        org.apache.tomcat.util.http.fileupload.IOUtils.copy(fileStream, response.getOutputStream());
        response.flushBuffer();
        fileStream.close();
    } catch (Exception e) {
        e.printStackTrace();
    }
    }

    @GetMapping("/delete/allFiles")
    public void deleteAll(){
        datafilesService.deleteAllFiles();
    }

    @PostMapping("/delete/file/{fileName:.+}")
    public void deletefile(@RequestParam("accessToken") String accessToken,
                           @PathVariable String fileName){
        datafilesService.deleteFile(fileName, accessToken);
    }
}
