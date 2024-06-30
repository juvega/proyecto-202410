import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductsComponent } from './products/products.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CategoriesComponent } from './categories/categories.component';
import { SalesComponent } from './sales/sales.component';
import { UsersComponent } from './users/users.component';
import { ManagementComponent } from './management/management.component';
import { AuthGuard } from './sigetra-auth.guard';
import { SigetraLoginComponent } from './sigetra-login/sigetra-login.component';

const routes: Routes = [
  { path: 'productos', component: ProductsComponent, canActivate: [AuthGuard]  },
  { path: 'dashboard', component: DashboardComponent, canActivate: [AuthGuard]  },
  { path: 'categorias', component: CategoriesComponent, canActivate: [AuthGuard]  },
  { path: 'ventas', component: SalesComponent, canActivate: [AuthGuard]  },
  { path: 'usuarios', component: UsersComponent, canActivate: [AuthGuard]  },
  { path: 'administracion', component: ManagementComponent, canActivate: [AuthGuard]  },
  { path: 'login', component: SigetraLoginComponent },
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: '**', redirectTo: '/login' }
];



@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
