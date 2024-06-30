import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '@auth0/auth0-angular';

@Component({
  selector: 'app-sigetra-login',
  templateUrl: './sigetra-login.component.html',
  styleUrls: ['./sigetra-login.component.scss']
})
export class SigetraLoginComponent implements OnInit  {
  isAuthenticated: boolean = false;
  constructor(public auth: AuthService, private router: Router) {}
  

  
  ngOnInit(): void {
    this.auth.isAuthenticated$.subscribe(isAuthenticated => {
      this.isAuthenticated = isAuthenticated;
      if (this.isAuthenticated) {
        this.router.navigate(['/dashboard']);
      }
    });
  }

  login(): void {    
    this.auth.loginWithRedirect();
  }
}
