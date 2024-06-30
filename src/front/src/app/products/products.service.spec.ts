import { TestBed } from '@angular/core/testing';

import { ProductsService as ProductsService } from './products.service';

describe('ProductoService', () => {
  let service: ProductsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProductsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
