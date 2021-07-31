# Deploying frontend

Well, it's a mess. For some reason I failed to do it on my server using docker. The unsecure `http` worked while I was unable to correctly install the SSL certificates and combine them with nginx and docker to make the `https` work.

# Alternatives

## Firebase

Great, easy and free tool for deployment. And it actually surprisingly works without bullshit. Also super easy user interface. The deployment has a default `https` connection.

I followed [this tutorial](http://appsology.co.uk/dwt/vue-js-tutorial/), but here are the steps:

1. Create a new project on firebase.
2. Install firbase tools if you haven't already.

```bash
npm install -g firebase-tools
```

3. Login.

```bash
firebase login
```

4. Initialize firebase from projects' root directory.

```bash
firebase init
```

5. Firebase will ask you some questions:
   - Select **hosting**.
   - Select to chose an **existing project**.
   - Set public directory to **dist**.
   - Choose yes for **single page html**.
6. Build project.

```bash
npm run build
```

7. Deploy.

```bash
firebase deploy --only hosting
```

## Github pages

Looks seriously amazing **BUT** I could not get it to work.
Vue has this `vue.config.js` configuration file

```js
module.exports = {
  // publicPath: '/metuljmania-app-gui/'
  publicPath: "/",
};
```

which I think is also important why it didn't work.

> Homepage always worked, but any subpages did not! No idea why.

# Keep an eye on

## Caddy server

The [Caddy](https://caddyserver.com/docs/getting-started) was recommended to me. It looks simple but I never tried it.

- Default SSL support.
- Easy installation.

## Docker Swarm

The [Docker Swarm](https://dockerswarm.rocks) seems to be very powerful too. A simpler alternative to kubernetess. However, I was not able to use it as it kept complaining that the port 80 is busy.

- Powerful.
- Default SSL support.
