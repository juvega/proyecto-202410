import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { provideAuth0 } from '@auth0/auth0-angular';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { provideHttpClient } from '@angular/common/http';
import { ProductsService } from './products/products.service';
import { SigetraMenuComponent } from './sigetra-menu/sigetra-menu.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CategoriesComponent } from './categories/categories.component';
import { SalesComponent } from './sales/sales.component';
import { UsersComponent } from './users/users.component';
import { ManagementComponent } from './management/management.component';
import { CommonModule } from '@angular/common';
import { ProductsComponent } from './products/products.component';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    SigetraMenuComponent,
    DashboardComponent,
    CategoriesComponent,
    SalesComponent,
    UsersComponent,
    ManagementComponent,
    ProductsComponent
  ],
  imports: [    
    BrowserModule,
    AppRoutingModule,
    CommonModule,
    FormsModule,
    NgbModule
  ],
  providers: [
    provideHttpClient(),
    ProductsService,
    provideAuth0({
      domain: 'dev-caf2q4ut5m4pp4rz.us.auth0.com',
      clientId: 'c9ay37UI2p8HzTTiNXFIzAHllwMZjN7K',
      authorizationParams: {
        redirect_uri: window.location.origin,
      },
    })
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
