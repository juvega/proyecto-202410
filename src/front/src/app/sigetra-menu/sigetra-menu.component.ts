import { Component, OnInit } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';

@Component({
  selector: 'app-sigetra-menu',
  templateUrl: './sigetra-menu.component.html',
  styleUrls: ['./sigetra-menu.component.scss']
})
export class SigetraMenuComponent implements OnInit {
  isAuthenticated: boolean = false;
  
  constructor(public auth: AuthService) {}

  ngOnInit(): void {
    this.auth.isAuthenticated$.subscribe(isAuthenticated => {
      this.isAuthenticated = isAuthenticated;
    });
  }
  
  logout(): void {
    this.isAuthenticated = false;    
    this.auth.logout();
  }
}
