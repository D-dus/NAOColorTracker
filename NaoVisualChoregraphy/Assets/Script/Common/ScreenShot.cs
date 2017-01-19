using UnityEngine;
using UnityEngine.UI;
using System.Collections;
using System;

public class ScreenShot : MonoBehaviour
{
	[SerializeField]
	private Camera OVcamera;

	private byte[] mBufferToSend;
	private Texture2D imageOverview;
	private Rect CameraRect;
	private RenderTexture currentRT;

	private System.Object lockThis;


	public void FixeData()
	{
		lock (lockThis) {
			currentRT = RenderTexture.active;
			RenderTexture.active = OVcamera.targetTexture;
			OVcamera.Render ();
			imageOverview.ReadPixels (CameraRect, 0, 0);
			imageOverview.Apply ();
			RenderTexture.active = currentRT;
			mBufferToSend = imageOverview.EncodeToJPG ();
		}
	}
	void Start()
	{
		imageOverview = new Texture2D(OVcamera.targetTexture.width, OVcamera.targetTexture.height, TextureFormat.RGB24, false);
		CameraRect = new Rect (0, 0, OVcamera.targetTexture.width, OVcamera.targetTexture.height);
		lockThis = new System.Object ();
	}

	void Update()
	{
		FixeData ();
	}
	public byte[] GetBufferToSend()
	{
		return mBufferToSend;
	}

}