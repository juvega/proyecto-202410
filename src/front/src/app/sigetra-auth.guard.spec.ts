import { TestBed } from '@angular/core/testing';
import { CanActivateFn } from '@angular/router';

import { sigetraAuthGuard } from './sigetra-auth.guard';

describe('sigetraAuthGuard', () => {
  const executeGuard: CanActivateFn = (...guardParameters) => 
      TestBed.runInInjectionContext(() => sigetraAuthGuard(...guardParameters));

  beforeEach(() => {
    TestBed.configureTestingModule({});
  });

  it('should be created', () => {
    expect(executeGuard).toBeTruthy();
  });
});
