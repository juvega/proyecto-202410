import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductsComponent } from './products/products.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CategoriesComponent } from './categories/categories.component';
import { SalesComponent } from './sales/sales.component';
import { UsersComponent } from './users/users.component';
import { ManagementComponent } from './management/management.component';

const routes: Routes = [
  { path: 'productos', component: ProductsComponent },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'categorias', component: CategoriesComponent },
  { path: 'ventas', component: SalesComponent },
  { path: 'usuarios', component: UsersComponent },
  { path: 'administracion', component: ManagementComponent },
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' }
];



@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
