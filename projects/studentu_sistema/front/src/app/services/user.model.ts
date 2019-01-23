export class User {
  userName: string;
  password: string;
  email: string;
  firstName: string;
  lastName: string;
  university: string;

  constructor(json: any) {
    if (json != null) {
      this.userName = json.userName;
      this.password = json.password;
      this.email = json.email;
      this.firstName = json.firstName;
      this.lastName = json.lastName;
      this.university = json.university;
    }
  }

}
