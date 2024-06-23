import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';
import { provideAuth0 } from '@auth0/auth0-angular';

const combinedConfig = {
  ...appConfig,
  providers: [
    ...appConfig.providers,
    provideAuth0({
      domain: 'dev-caf2q4ut5m4pp4rz.us.auth0.com',
      clientId: 'c9ay37UI2p8HzTTiNXFIzAHllwMZjN7K',
      authorizationParams: {
        redirect_uri: window.location.origin,
      },
    }),
  ],
};

bootstrapApplication(AppComponent, combinedConfig)
  .catch((err) => console.error(err));