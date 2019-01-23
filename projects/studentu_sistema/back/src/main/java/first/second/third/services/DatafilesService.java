package first.second.third.services;

import first.second.third.beans.documents.Datafiles;
import first.second.third.beans.documents.User;
import first.second.third.beans.response.FilenamesResponse;
import first.second.third.repositories.DatafilesRepository;
import first.second.third.repositories.UserRepository;
import org.bson.BsonBinarySubType;
import org.bson.types.Binary;
import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class DatafilesService {

    @Autowired
    private DatafilesRepository datafilesRepository;
    private UserRepository userRepository;

    public String fileUpload(MultipartFile multipart, String username, String faculty, String subject){
        try {
            String fileName = multipart.getOriginalFilename();
            Datafiles datafileInDB = datafilesRepository.findDatafilesByFileName(fileName);
            if(datafileInDB!=null){
            if(datafileInDB.getSubject().equals(subject)){
                return "Failas tokiu pavadinimu jau egzistuoja";
            }
            }
            Datafiles newFile = new Datafiles();
            newFile.setTimeStamp(LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")));
            newFile.setFile(new Binary(BsonBinarySubType.BINARY, multipart.getBytes()));
            newFile.setFileName(fileName);
            newFile.setContentType(multipart.getContentType());
            newFile.setUserName(username);
            newFile.setFaculty(faculty);
            newFile.setSubject(subject);
            datafilesRepository.save(newFile);
            return "Failas įkeltas sėkmingai";
        } catch (Exception e){
            e.printStackTrace();
            return "Klaida";
        }
    }


    public Datafiles getDatafileGetByFilename(String fileName){
        Datafiles datafile = datafilesRepository.findDatafilesByFileName(fileName);
        return datafile;
    }


    public List<FilenamesResponse> getFilesFilenames(String subject){
        return (datafilesRepository.findDatafilesBySubject(subject)).stream()
                .map(FilenamesResponse::new)
                .collect(Collectors.toList());
    }

    public List<FilenamesResponse> getFilesFilenamesByUserName(String userName){
        return (datafilesRepository.findDatafilesByUserName(userName)).stream()
                .map(FilenamesResponse::new)
                .collect(Collectors.toList());
    }

    public void deleteAllFiles(){ datafilesRepository.deleteAll();}

    public void deleteFile(String fileName, String accessToken){
        Datafiles datafile = datafilesRepository.findDatafilesByFileName(fileName);
        User user = userRepository.getUserByUserName(datafile.getUserName());
        if (user.getAccessToken() == accessToken){
            datafilesRepository.delete(datafile);
        }
    }

}
