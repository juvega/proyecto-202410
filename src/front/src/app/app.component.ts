import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { AuthService } from '@auth0/auth0-angular';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {  
  title = 'sigetra';
  constructor(public auth: AuthService) {}
}
